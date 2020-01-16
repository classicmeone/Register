

from azure.storage.blob import BlockBlobService, PublicAccess
from datetime import date,datetime timedelta
from pandas import date_range


class Videos(object):
    pass
'''
    def __init__(self, start_date, end_date):
        self.date_start = start_date
        self.date_end = end_date
     

    def _container_access(self):
        
        blob_service = BlockBlobService(account_name = 'dataandaistorageacct', 
                                        account_key = 'U+r4S1a+UPiRc/YOAntraxQk0e/b0WJNz0CK/NLwaNQYVwYtXTpzJxUqB9UHjz/D82nwLxjhjpKviVKTvGYKcg==')
        container = 'data'
        blob_service.set_container_acl(container, public_access = PublicAccess.Container)
        return blob_service, container

    
    def _list_dates(self):
       date_list = []
       pandas_date = date_range(start_date, end_date).to_pydatetime().tolist()
       for each in pandas_date:
           date_list.append(each.strftime("%Y-%m-%d")
       return date_list
   
    
    def _get_blobs(self, date_list, folder_name):
        blob_service, container = self._container_access()
        blobs = list(blob_service.list_blobs(container))
        return blobs
    
    
    def _list_blob():
        date_list = self._list_dates()
        blob_list = self._get_blobs()
        blobs = []
        for blob in blob_list:
            for each_date in date_list:
                if each_date in blob.name:
                    blobs.append(blob.name)
                    break
        return blobs
            
     
    def blob_video(self):
        blob_service, container = self._container_access()
        blob_videos = []
        blob_list = self._list_blobs()
        for blob in blob_list:
            blob_videos.append(blob_service.make_blob_url(container, blob))
        return blob_videos
'''




     

    
    
   
