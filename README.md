# ChannelService test task

<hr>

To run the application, you need to agree on steps:
* Clone project <br>
    git clone https://github.com/ck1e/ChannelService.git 
* Go to the project folder <br>
    cd <...>/ChannelService
* Install all dependencies <br>
    pip install -r requirements.txt
* Create a Postgres database for this project
* In the file "./configs/db.py", enter your data for the database
* Add your address (necessarily http<b>S</b>) to the file "configs/local.py" in ALLOWED_HOSTS
* Replace address with WEBHOOK_ADDRESS in file "ordersOnlineUpdates/apps.py"
* Then you need to get the following accesses:
  * client-secret
  * service-account
  * token  <br>
    This is done in https://console.cloud.google.com
* Then you can run the application <br>
    python manage.py runserver localhost:8000 <br>
    When you first start you are asked to confirm authorization in Google

<h3><b>PS. File "ordersOnlineUpdates/apps.py" contains all related settings for the application</b></h3>