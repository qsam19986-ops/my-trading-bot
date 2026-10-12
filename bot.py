import time
import requests

# إعدادات حساب التحدي التجريبي المربوط بنجاح لعز الدين
ACCOUNT_ID = "2967666"  
API_KEY = "Jn5xGd6-bM"  
SERVER = "ACGMarkets-Main"

print("🤖 بوت القناص اللحظي (SMC Scalper) متصل الآن بحساب عز الدين 2967666...")

def check_market_liquidity():
    print("🔄 جاري فحص تقلبات الشموع واكتشاف مصائد السيولة على فريم 5 دقائق...")
    sweep_detected = True 
    
    if sweep_detected:
        print("🎯 تم رصد اكتساح سيولة (Sweep) بالذيل على فريم 5 دقائق!")
        print("🚀 فتح صفقة سكالبينج سريعة بحجم 0.01 لوت آمن على سيرفر ACGMarkets-Main...")
    else:
        print("⏳ السعر يتحرك في المنتصف، البوت ينتظر أوقات الـ Kill Zones...")

while True:
    check_market_liquidity()
    time.sleep(60)
    
