# ☀️ Quyosh Panellari Xizmat Bot

Bu Telegram bot quyosh panellariga xizmat ko‘rsatuvchi korxona uchun mo‘ljallangan. Bot orqali mijozlar xizmat buyurtma qilishlari, texnik xizmat holatini tekshirishlari va qo‘shimcha ma’lumot olishlari mumkin.

---

## 📌 Asosiy funksiyalar

- 📋 Xizmatlarga buyurtma berish (o‘rnatish, tekshiruv, tozalash, almashtirish)
- 📆 Texnik xizmat uchun navbatga yozilish
- 📡 Mavjud xizmat turlarini ko‘rish
- 📞 Operator bilan bog‘lanish (aloqa ma'lumotlari)
- 🧾 Mijozga xizmat tarixini ko‘rsatish

---

## ⚙️ Texnologiyalar

- Python 3.x
- [Aiogram](https://github.com/aiogram/aiogram) (Telegram bot framework)
- PostgreSQL yoki SQLite (ma'lumotlar bazasi)
- Redis (ixtiyoriy — navbat, seanslar uchun)
- Docker (deploy uchun, ixtiyoriy)

---

## 🚀 O‘rnatish

### 1. Repozitoriyani klon qiling:

```bash
git clone https://github.com/bunyod-abdulloh/bnpzbot.git
cd bnpzbot
```

### 2. Virtual muhit yarating va faollashtiring:

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```

### 3. Kerakli kutubxonalarni o‘rnating:

```bash
pip install -r requirements.txt
```

### 4. `.env` fayl yarating va quyidagilarni kiriting:

```env
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=sqlite:///db.sqlite3
ADMINS=123456789
```

### 5. Botni ishga tushiring:

```bash
python main.py
```

---

## 🎯 Maqsadli foydalanuvchilar

- Quyosh panellari o‘rnatish va texnik xizmat bilan shug‘ullanuvchi xodimlar
- Hududiy dilerlar va servis markazlari
- Yakuniy mijozlar (aholi va korxonalar)

---

## 📞 Bog‘lanish

Agar sizda savollar, takliflar yoki texnik muammolar bo‘lsa, quyidagi manzillarga murojaat qiling:


---

## 📝 Litsenziya

Ushbu loyiha ochiq manba (open-source) sifatida ishlab chiqilgan.  
Litsenziya: MIT

---

## 👨‍💻 Muallif

**Bunyod Abdulloh**  
GitHub: [https://github.com/bunyod-abdulloh](https://github.com/bunyod-abdulloh)
