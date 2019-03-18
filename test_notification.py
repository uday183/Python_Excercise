from pyfcm import FCMNotification
push_service = FCMNotification(api_key="AIzaSyCeOwUe2Al7sTQCIbm5IlHLa_x1V1DM7qA")

# OR initialize with proxies
 
proxy_dict = {
          "http"  : "http://172.25.12.39:8001"
        }
push_service = FCMNotification(api_key="AIzaSyCeOwUe2Al7sTQCIbm5IlHLa_x1V1DM7qA", proxy_dict=proxy_dict)
 
# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
 
registration_id = "dv41o2Fs9MY:APA91bHc0eZBC0VqrMf2c14L9nz3Offm0yKRd9Q2ATb74zHdrcUm0ka53OWYANEyy0QMV4vUuzCJ2W1w7j71KEV6dHcEvrSF-I45Zr7XcwvfFYvTc1bnojTWl2yFmtotH-WdL5OtxuIB_Dch5FmYQysY7rzHQC-Ylg"
message_title = "uday notification"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
 
print (result)
 
