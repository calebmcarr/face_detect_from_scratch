import numpy as np
from numpy import linalg as lg
import cv2
import os

class setup:
    '''Creates a basis for the image set that main is pointed to.
       Images must all have the same dimensions.'''
    def __init__(self):
        self.main()
            
    def cov_mat(self,diff_vecs):
        '''create the covariance matrix and return the eigenvalues and eigenvectors'''
        self.diff_vecs_mat = lg.matrix(diff_vecs)
        self.dvm_trans = self.diff_vecs_mat.transpose()
        self.eigenspace = lg.eig(self.dvm_trans*self.diff_vecs_mat)
        self.eigenvalues = self.eigenspace[0]
        self.eigenvectors = self.eigenspace[1]
        return self.eigenvalues,self.eigenvectors
            
    def diff_vec(self,photo,avg_face):
        '''Return the difference vector, phi'''
        phi = []
        for i in range(len(photo)):
            for j in range(len(photo[i])):
                phi.append(photo[i]-avg_face[i])
        return phi
        
    def avg_face(self, photos):
        '''makes average face, psi, out of set of vectors, gamma.'''
        self.avg_face = []
        for i in range(len(photos[0])):
            self.sum = 0
            for j in range(len(photos)):
                self.sum+=photos[j][i]
            self.avg_face.append(self.sum/len(self.photos))
        return self.avg_face
                
           
    def im_to_vec(self,root):
        '''Turns some n x m image into a nm x 1 vector'''
        im = cv2.imread(root,cv2.IMREAD_GRAYSCALE)
        dim = len(im)*len(im[0])
        g = []
        for i in range(len(im)):
            for j in range(len(im[0])):
                g.append(im[i][j])
        return g

    def main(self):
        #Specifiy the folder where the database is and get all the photos
        self.root = 'D:\\Python\\photos'
        self.photos = os.listdir(self.root)
        #list to hold all the images -> vectors
        self.photos_to_vec = []
        #list for the average face
        self.avg_face = []
        #list for difference vectors
        self.diff_vec = []
        #allocate variable for the eigenvectors and eigenvalues
        eigenvalues = 0
        eigenvectors = 0
        #Turn every image into a mn x 1 vector rather than a n x m matrix
        for i in range(len(self.photos)):
            self.file = self.root+'\\'+self.photos[i]
            self.photos_to_vec.append(self.im_to_vec(self.file))
            #print len(self.photos_to_vec[i])
        #create the average image
        self.avg_face = avg_face(self.photos_to_vec)
        #create the difference vectors
        for i in range(len(self.photos_to_vec)):
            self.diff_vec.append(self.diff_vec(self.photos_to_vec[i]))
        #get the values for space face
        eigenvalues,eigenvectors = self.cov_mat(self.diff_vec)
        #return eigenvalues,eigenvectors