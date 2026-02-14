import os
import time

# مصفوفة الحزم لسهولة التعديل عليها
PACKAGES = [
    "python", "python-pip", "git", "php", "nano", "nmap", 
    "perl", "ruby", "golang", "host", "hydra", "wget", 
    "net-tools", "w3m", "unrar", "clang", "openssh", 
    "tor", "tar", "zip", "proot", "figlet", "cowsay", "toilet"
]

def clear():
    os.system("clear")

def logo():
    print("\033[1;32m") # اللون الأخضر
    print("""
    =======================================
    |       AMF - YEMEN TECH 2026         |
    =======================================
    | Telegram: @Professionaltermux       |
    | المطور: تحسين الجيل القادم           |
    =======================================""")

def install_basics():
    print("\n\033[1;34m[*] جاري بدء عملية التثبيت الشاملة...\033[0m")
    
    # تحديث المستودعات أولاً
    print("[+] تحديث النظام...")
    os.system("pkg update -y && pkg upgrade -y")
    
    # تثبيت الحزم دفعة واحدة لتسريع العملية
    all_pkgs = " ".join(PACKAGES)
    print(f"[+] جاري تثبيت {len(PACKAGES)} حزمة أساسية...")
    os.system(f"pkg install {all_pkgs} -y")
    
    # تثبيت مكتبات بايثون و Ruby
    print("[+] تثبيت المكتبات البرمجية...")
    os.system("pip install requests wget wheel")
    os.system("gem install lolcat")
    
    print("\n\033[1;32m[✓] تم تثبيت جميع الأساسيات بنجاح!\033[0m")
    time.sleep(2)

def main():
    while True:
        clear()
        logo()
        print("\n[1] تثبيت أساسيات الترمكس (المطور)")
        print("[2] فحص حالة النظام")
        print("[00] خروج")
        
        choice = input("\nAMF-PRO#: ")
        
        if choice == "1":
            confirm = input("\n[?] هل تريد الاستمرار؟ عملية التثبيت تستهلك بيانات (y/n): ")
            if confirm.lower() == 'y':
                install_basics()
                input("\nاضغط Enter للعودة للقائمة...")
        
        elif choice == "2":
            print("\n[!] معلومات النظام:")
            os.system("uname -a")
            input("\nاضغط Enter للعودة...")
            
        elif choice == "00":
            print("\nوداعاً يا صديقي.. بالتوفيق في رحلتك البرمجية!")
            break
        else:
            print("\n[!] خيار خاطئ، حاول مرة أخرى.")
            time.sleep(1)

if __name__ == "__main__":
    main()
