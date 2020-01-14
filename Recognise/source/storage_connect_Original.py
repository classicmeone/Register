

from azure.storage.blob import BlockBlobService, PublicAccess
from datetime import date, timedelta


class Videos(object):
    
    def __init__(self, start_date, end_date):
        self.date_start = start_date
        self.date_end = end_date
     
    
    def _list_dates(self):
       delta = self.date_end - self.date_start
       date_list = []
       for count in range(delta.days + 1):
           date_list.append(self.date_start + timedelta(days = count))
       return date_list
   
    
    def _container_access(self):
        blob_service = BlockBlobService(account_name = 'dataandaistorageacct', 
                                        account_key = 'U+r4S1a+UPiRc/YOAntraxQk0e/b0WJNz0CK/NLwaNQYVwYtXTpzJxUqB9UHjz/D82nwLxjhjpKviVKTvGYKcg==')
        container = 'data'
        blob_service.set_container_acl(container, public_access = PublicAccess.Container)
        return blob_service, container
    
   
    def _folder_blobs(self, date_list, folder_name):
        folder_blobs = []
        blob_service, container = self._container_access()
        blob_list = blob_service.list_blobs(container, prefix = folder_name)
        for blob in blob_list:
            for each_date in date_list:
                if str(each_date) in blob.name:
                    
                    folder_blobs.append(blob.name)
                    date_list.remove(each_date)
                    break
            if not date_list:
                
                break
        return folder_blobs
    
    
    def _date_categories(self, date_list):
        category_date = {}
        for each_date in date_list:
            if each_date.year in category_date.keys():
                category_date[each_date.year].append(each_date)
            else:
                category_date[each_date.year] = [each_date]
        return category_date
    
    
    def _blob_list(self):
        blob_list = []
        date_list = self._list_dates()
        category_date = self._date_categories(date_list)
        for key, value in category_date.items():
            blob_list.extend(self._folder_blobs(value, key))
        return blob_list
            
     
    def blob_video(self):
        blob_videos = []
        blob_service, container = self._container_access()
        blob_list = self._blob_list()
        for blob in blob_list:
            blob_videos.append(blob_service.make_blob_url(container, blob))
        return blob_videos



   
##v = Videos(date(2018,10,20), date(2018,10,25))
#print(v.blob_video())
     

    
    
   
