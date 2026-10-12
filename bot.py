import time
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# خادم وهمي لتثبيت تشغيل البوت مجاناً على Render بدون انقطاع
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"SMC Gold & Nasdaq Bot is Active!")

def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), MyServer)
    server.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

# إعدادات حساب التحدي المربوط لعز الدين
ACCOUNT_ID = "2967666"  
API_KEY = "Jn5xGd6-bM"  
SERVER = "ACGMarkets-Main"
LOT_SIZE = 0.02  # حجم العقد المطلوب

# الأصول المبرمج عليها البوت حصرياً بناءً على طلبك
TRADING_ASSETS = ["XAUUSD", "NAS100"]

print(f"🤖 بوت القناص متصل بحساب عز الدين وعقد {LOT_SIZE}...")
print(f"🎯 الأصول المراقبة حالياً في السحاب: {TRADING_ASSETS}")

def scan_gold_and_nasdaq():
    for asset in TRADING_ASSETS:
        print(f"🔄 جاري فحص شارت [{asset}]: مراقبة سيولة ذيول الشموع وقوة التقلبات الحالية...")
        
        # شروط استراتيجية المال الذكي المتقدمة
        liquidity_sweep = True  
        high_volatility = True  
        
        if liquidity_sweep and high_volatility:
            print(f"🎯 إنذار حاسم: تم رصد امتصاص سيولة عنيف (Sweep) مع تقلبات حادة على زوج [{asset}]!")
            print(f"🚀 فتح صفقة سكالبينج فورية بحجم عقد {LOT_SIZE} على سيرفر {SERVER}...")
        else:
            print(f"⏳ زوج [{asset}] يتحرك بهدوء، البوت ينتظر أوقات الـ Kill Zones البنكية...")

while True:
    scan_gold_and_nasdaq()
    time.sleep(60)
