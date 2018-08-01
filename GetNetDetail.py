import sys
import numpy as np
np.set_printoptions(threshold=np.inf) #Set the how your print command will look like
import caffe

caffe.set_mode_cpu()


def Get_NetParam(caffe_root, net_name, result_path):
    caffe_model = caffe_root + 'models/bvlc_' + net_name + '/bvlc_' + net_name + '.caffemodel'#Load the .caffemodel file
    deploy_proto = caffe_root + "models/bvlc_"+ net_name +"deploy.prototxt"#Load deploy.prototxt
    net = caffe.Net(deploy_proto,caffe_model,caffe.TEST) #Get the Net

    file_param = result_path + net_name + '_params.txt'
    for layer_name, param in net.params.iteritems():#Get the parameters of each layer(W and b)
        with open(file_param,'a') as f:
            f.write(layer_name + '_W:\n' + str(param[0].data) + layer_name + '_b:\n' + str(param[1].data))

    file_blob = result_path + net_name + '_blobs.txt'
    for layer_name, blob in net.blobs.iteritems():#Get the features of each layer
        with open(file_blob,'a') as f:
            f.write(layer_name + str(blob.data))


if __name__ == '__main__':
    if(len(sys.argv) < 4):
	print ("Please input correct parameters")
	exit()

    caffe_root = sys.argv[1]#caffe_root
    net_name = sys.argv[2]#The name of net
    result_path = sys.argv[3]#The path you want to save the results

    Get_NetParam(caffe_root, net_name, result_path)  
