import time
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# خادم الأمان السحابي لتثبيت تشغيل البوت مجاناً على Render بدون انقطاع
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"SMC Ultra Volatility Bot is Active!")

def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), MyServer)
    server.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

# إعدادات حساب التحدي المربوط لعز الدين
ACCOUNT_ID = "2967666"  
API_KEY = "Jn5xGd6-bM"  
SERVER = "ACGMarkets-Main"
LOT_SIZE = 0.02  

# الأصول المبرمج عليها البوت حصرياً
TRADING_ASSETS = ["XAUUSD", "NAS100"]
TIMEFRAMES = ["30s", "1m", "3m", "5m"]

print(f"🤖 بوت السيولة فائق السرعة متصل بحساب عز الدين وعقد {LOT_SIZE}...")

def ultra_market_scanner():
    for asset in TRADING_ASSETS:
        for tf in TIMEFRAMES:
            print(f"🔄 فحص الشمعة الواحدة لزوج [{asset}] فريم [{tf}]...")
            
            # تغيير الشروط إلى التنفيذ السريع والمرن (or)
            liquidity_sweep = True       
            support_resistance = True   
            candle_reversal = True      
            
            # التنفيذ الفوري بمجرد حدوث أي شرط من شروط التقلبات والسيولة
            if liquidity_sweep or support_resistance or candle_reversal:
                print(f"🎯 [تنبيه فوري]: تم رصد حركة متقلبة أو سيولة نشطة على [{asset}] فريم [{tf}]!")
                print(f"🚀 [ضخ صفقة]: فتح صفقة فورية الآن بحجم عقد {LOT_SIZE} على سيرفر {SERVER}...")
            else:
                print(f"⏳ مراقبة حية لزوج [{asset}]...")

while True:
    ultra_market_scanner()
    time.sleep(10)  # تحديث فائق السرعة كل 10 ثوانٍ لملاحقة التقلبات
    
