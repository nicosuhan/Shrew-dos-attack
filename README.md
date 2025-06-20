# Shrew DoS Attack

## 📘 Descriere generală

Atacul **Shrew** (sau *Low-Rate TCP-Targeted DoS*) este un tip sofisticat de atac de tip Denial-of-Service. În loc să inunde rețeaua cu trafic masiv, acest atac trimite rafale scurte și bine temporizate de trafic pentru a exploata mecanismul de control al congestiei din TCP.

---

## ⚙️ Cum funcționează?

1. **Exploatarea mecanismului RTO din TCP**  
   TCP (Transmission Control Protocol) intră într-o stare de „timeout” dacă nu primește confirmare pentru un pachet transmis. Acest timeout (RTO – Retransmission Timeout) este de aproximativ 1 secundă. Atacul Shrew vizează exact acest mecanism.

2. **Model de atac tip „square wave”**  
   Atacatorul trimite o rafală scurtă de trafic care umple buffer-ul routerului, cauzând pierderi de pachete. Imediat după, atacul se oprește. Când traficul legitim încearcă să revină, din cauza RTO-ului, este blocat sau încetinit. Acest ciclu se repetă regulat.

3. **Trafic redus, impact mare**  
   Chiar dacă traficul generat de atac este scăzut în medie, impactul asupra performanței rețelei este major – fluxurile TCP legitime pot fi reduse la doar 10-15% din capacitatea normală.

---

## 📊 Parametrii principali ai atacului

- **T (Perioada atacului):** Intervalul total între două rafale. Trebuie să coincidă cu RTO-ul fluxului țintit (~1 sec).
- **L (Durata rafalei):** Foarte scurtă (ex: 50–100 ms).
- **R (Rata în timpul rafalei):** Suficient de mare pentru a congestiona bufferul.

---

## 💥 Efecte asupra traficului TCP

- Blocarea traficului legitim fără a detecta un volum anormal.
- Reducerea semnificativă a lățimii de bandă.
- Degradarea experienței utilizatorilor (încetinirea încărcării paginilor, întreruperi în aplicații web sau VoIP).

---

## 🕵️‍♀️ De ce e greu de detectat?

- **Rată medie scăzută:** Nu atrage atenția sistemelor de detecție bazate pe volum.
- **Comportament periodic:** Poate fi detectat doar cu analiză spectrală sau metode statistice.
- **Se amestecă ușor cu traficul legitim:** Rafalele pot arăta ca fluctuații normale de trafic.

---

## 🛡️ Metode de detectare și protecție

### 🔎 Analiză spectrală
Transformarea semnalului de trafic în domeniul frecvenței permite detectarea caracteristicii periodice a atacului.

### 🔗 CDF (Collaborative Detection and Filtering)
Sistem distribuit care identifică și filtrează fluxurile suspecte pe baza analizelor făcute în mai multe puncte din rețea.

### ⚙️ Ajustări în TCP
- Randomizarea RTO-ului pentru a rupe sincronizarea atacului.
- Reducerea ferestrei de timeout pentru a permite revenirea mai rapidă a traficului legitim.

### 🎛️ QoS și Machine Learning
- Aplicarea de politici inteligente per flux.
- Identificarea comportamentului anormal folosind clasificatori ML.

---

## ✅ Rezumat

| Caracteristică           | Shrew DoS Attack             |
|--------------------------|------------------------------|
| Tip atac                 | Low-rate, periodic           |
| Exploatează              | Timeout-ul TCP (RTO)         |
| Detectabil prin          | Analiză spectrală, CDF       |
| Rată medie trafic        | Foarte redusă                |
| Impact asupra TCP        | Major, reduce drastic debitul|
