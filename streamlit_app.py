import ee
import os

# 1. Siz taqdim etgan servis hisobi ma'lumotlari
# Eslatma: 'private_key' qismini to'liq holda o'zgaruvchiga kiriting
SERVICE_ACCOUNT = 'geouser111@fluted-house-483917-g9.iam.gserviceaccount.com'
KEY_DATA = """-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC0xvcWHvdZ01oh
... (bu yerga JSON fayldagi to'liq private_key ni qo'ying) ...
-----END PRIVATE KEY-----"""

# 2. Autentifikatsiya qilish
try:
    credentials = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, key_data=KEY_DATA)
    ee.Initialize(credentials)
    print("Google Earth Engine muvaffaqiyatli ishga tushirildi!")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 3. Namuna: Farg'ona mintaqasi uchun bo'sh filtr yaratish (Geologik tahlil uchun)
# Bu yerda siz keyinchalik neft va gaz konlari xaritasini yuklashingiz mumkin
fergana_region = ee.Geometry.Rectangle([70.0, 40.0, 72.5, 41.0]) 

# Yer sathi tasvirini olish (masalan, Landsat 8)
image = ee.ImageCollection("LANDSAT/LC08/C01/T1_SR") \
    .filterBounds(fergana_region) \
    .sort('CLOUD_COVER') \
    .first()

print(f"Tanlangan tasvir ID raqami: {image.id().getInfo()}")
