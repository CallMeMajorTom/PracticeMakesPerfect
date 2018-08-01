import sys
import numpy as np # linear algebra
import skimage, os
from skimage.morphology import ball, disk, binary_erosion, remove_small_objects, erosion, closing, binary_closing
from skimage.measure import label,regionprops
from skimage.filters import roberts
from skimage import measure
from skimage.segmentation import clear_border
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import SimpleITK as sitk


'''
This funciton reads a '.mhd' file using SimpleITK and return the image array,
origin and spacing of the image.
'''
def load_itk(filename):
    # Reads the image using SimpleITK
    itkimage = sitk.ReadImage(filename)

    # Convert the image to a  numpy array first and then shuffle the dimensions to get axis in the order z,y,x
    ct_scan = sitk.GetArrayFromImage(itkimage)

    # Read the origin of the ct_scan, will be used to convert the coordinates from world to voxel and vice versa.
    origin = np.array(list(reversed(itkimage.GetOrigin())))

    # Read the spacing along each dimension
    spacing = np.array(list(reversed(itkimage.GetSpacing())))

    return ct_scan, origin, spacing

'''
This funciton reads all '.mhd' files under a folder
'''
def read_ct_scan(folder_name):
        # Read the slices from the folder
        slices = []
        for filename in os.listdir(folder_name):
             if os.path.splitext(filename)[1] == ".mhd":
                 (ct_scan,_,_) = load_itk(folder_name + filename)
                 slices.append(ct_scan)

        return slices


def get_segmented_lungs(im, plot=False):

    '''
    This funtion segments the lungs from the given 2D slice.
    '''
    if plot == True:
        f, plots = plt.subplots(8, 1, figsize=(5, 40))
    '''
    Step 1: Convert into a binary image.
    '''
    binary = im < 604
    if plot == True:
        plots[0].axis('off')
        plots[0].imshow(binary, cmap=plt.cm.bone)
    '''
    Step 2: Remove the blobs connected to the border of the image.
    '''
    cleared = clear_border(binary)
    if plot == True:
        plots[1].axis('off')
        plots[1].imshow(cleared, cmap=plt.cm.bone)
    '''
    Step 3: Label the image.
    '''
    label_image = label(cleared)
    if plot == True:
        plots[2].axis('off')
        plots[2].imshow(label_image, cmap=plt.cm.bone)
    '''
    Step 4: Keep the labels with 2 largest areas.
    '''
    areas = [r.area for r in regionprops(label_image)]
    areas.sort()
    if len(areas) > 2:
        for region in regionprops(label_image):
            if region.area < areas[-2]:
                for coordinates in region.coords:
                       label_image[coordinates[0], coordinates[1]] = 0
    binary = label_image > 0
    if plot == True:
        plots[3].axis('off')
        plots[3].imshow(binary, cmap=plt.cm.bone)
    '''
    Step 5: Erosion operation with a disk of radius 2. This operation is
    seperate the lung nodules attached to the blood vessels.
    '''
    selem = disk(2)
    binary = binary_erosion(binary, selem)
    if plot == True:
        plots[4].axis('off')
        plots[4].imshow(binary, cmap=plt.cm.bone)
    '''
    Step 6: Closure operation with a disk of radius 10. This operation is
    to keep nodules attached to the lung wall.
    '''
    selem = disk(10)
    binary = binary_closing(binary, selem)
    if plot == True:
        plots[5].axis('off')
        plots[5].imshow(binary, cmap=plt.cm.bone)
    '''
    Step 7: Fill in the small holes inside the binary mask of lungs.
    '''
    edges = roberts(binary)
    binary = ndi.binary_fill_holes(edges)
    if plot == True:
        plots[6].axis('off')
        plots[6].imshow(binary, cmap=plt.cm.bone)
    '''
    Step 8: Superimpose the binary mask on the input image.
    '''
    get_high_vals = binary == 0
    im[get_high_vals] = 0
    if plot == True:
        plots[7].axis('off')
        plots[7].imshow(im, cmap=plt.cm.bone)

    return im


def segment_lung_from_ct_scan(ct_scan):
    return np.asarray([get_segmented_lungs(slice) for slice in ct_scan])


def plot_ct_scan(scan):
    f, plots = plt.subplots(int(scan.shape[0] / 20) + 1, 4, figsize=(40, 40))
    for i in range(0, scan.shape[0], 5):
        plots[int(i / 20), int((i % 20) / 5)].axis('off')
        plots[int(i / 20), int((i % 20) / 5)].imshow(scan[i], cmap=plt.cm.bone)
    return plt

def plot_3d(image, threshold=-300):

    # Position the scan upright,
    # so the head of the patient would be at the top facing the camera
    p = image.transpose(2,1,0)
    p = p[:,:,::-1]

    verts, faces = measure.marching_cubes_classic(p, threshold)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Fancy indexing: `verts[faces]` to generate a collection of triangles
    mesh = Poly3DCollection(verts[faces], alpha=0.1)
    face_color = [0.5, 0.5, 1]
    mesh.set_facecolor(face_color)
    ax.add_collection3d(mesh)

    ax.set_xlim(0, p.shape[0])
    ax.set_ylim(0, p.shape[1])
    ax.set_zlim(0, p.shape[2])

    plt.show()



if __name__ == '__main__':
    if(len(sys.argv) < 4):
        print ("Please input correct parameters")
        exit()

    project_root =  sys.argv[1]
    luna_foldername = project_root + 'LUNA-subset0/'
    ct_scans = read_ct_scan(luna_foldername)
    i = 0
    for ct_scan in ct_scans:
        ct_scan += 1024
        segmented_ct_scan = segment_lung_from_ct_scan(ct_scan)
        plts = plot_ct_scan(segmented_ct_scan)
        imagepath = project_root + 'LUNA-result/' + str(i) + '.png'
        i = i + 1
        plts.savefig(imagepath)
        segmented_ct_scan[segmented_ct_scan < 604] = 0
        plot_ct_scan(segmented_ct_scan)
        ct_scan -= 1024

        selem = ball(2)
        binary = binary_closing(segmented_ct_scan, selem) #Closure operation with a ball of radius 2.
        ##Remove the largerst 2 connected component
        label_scan = label(binary)
        areas = [r.area for r in regionprops(label_scan)]
        areas.sort()
        for r in regionprops(label_scan):
            max_x, max_y, max_z = 0, 0, 0
            min_x, min_y, min_z = 1000, 1000, 1000

            for c in r.coords:
                max_z = max(c[0], max_z)
                max_y = max(c[1], max_y)
                max_x = max(c[2], max_x)

                min_z = min(c[0], min_z)
                min_y = min(c[1], min_y)
                min_x = min(c[2], min_x)
            if (min_z == max_z or min_y == max_y or min_x == max_x or r.area > areas[-3]):
                for c in r.coords:
                    segmented_ct_scan[c[0], c[1], c[2]] = 0
            else:
                index = (max((max_x - min_x), (max_y - min_y), (max_z - min_z))) / (min((max_x - min_x), (max_y - min_y) , (max_z - min_z)))
        plot_3d(segmented_ct_scan, 604)
