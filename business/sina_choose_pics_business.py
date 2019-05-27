# Author: SH
# Data: 2019/5/26
# Status 
# Comment:
from handle.sina_photo_album_handle import SinaPhotoAlbumHandle

class SinaChoosePicsBusiness(object):

    def __init__(self,driver):
        self.sp = SinaPhotoAlbumHandle(driver)

    def choose_pics(self):
        '''
        选择预定好的图片
        :return:
        '''
        self.sp.click_photo_album()
        self.sp.choose_photo_album()
        self.sp.choose_pics()
        self.sp.next()