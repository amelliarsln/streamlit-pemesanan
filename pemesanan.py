from turtle import home
import streamlit as st 
import tkinter as TK

st.sidebar.title("BURJO MEISYA SEMARANG")
st.sidebar.radio(("Kasir"),["A","B","C"])

test = st.sidebar.selectbox("Silahkan pilih", ['Home','Daftar Menu','Pemesanan'])

st.write("========================================================================================")

if test == 'Home':
    st.write("""#Halaman Login Kasir""") #menampilkan halaman utama
    with st.form(key ='my_key'): 
        username = st.text_input("Username")
        password = st.text_input("Password")
        st.form_submit_button("Login")
        
    st.date_input("tanggal sekarang")
    st.time_input("waktu sekarang")

    st.title("  BURJO MEISYA SEMARANG")
    
    st.subheader("Welcome")
    
    st.write("Burjo Meisya Semarang")
    
    st.write("Jl. Depan Gerbang Utama")

if test == 'Daftar Menu':
    st.header("Pilihan Menu Makanan:")
    st.subheader("INDOMIE (Custom)")
    st.write("1. mie tante Rp 7.000")
    st.write("2. mie telor Rp 10.000")
    st.write("3. mie dok-dok Rp 11.000")
    st.write("4. mie dok-dok ayam Rp 12.000")
    st.write("5. mie dok-dok sosis Rp 12.000")
    st.write("6. mie dok-dok baso Rp 12.000")
    st.write("7. mie dok-dok spesial Rp 14.000")
    st.write("8. mie spesial Rp 11.000")
    st.write("9. mie spesial ayam Rp 12.000")
    st.write("10. mie spesial sosis Rp 12.000")
    st.write("11. mie spesial baso Rp 12.000")

    st.subheader("NASI/TELOR/AYAM (Masakan)")
    st.write("1. omlet Rp 10.000")
    st.write("2. nasi omlet Rp 13.000")
    st.write("3. nasi gila Rp 14.000")
    st.write("4. nasi omlet ayam Rp 14.000")
    st.write("5. nasi omlet sosis Rp 14.000")
    st.write("6. nasi omlet baso Rp 14.000")
    st.write("7. nasi omlet spesial Rp 15.000")
    st.write("8. nasi sarden Rp 8.000")
    st.write("9. nasi sarden telor Rp 11.000")
    st.write("10. nasi telor Rp 8.000")
    st.write("11. nasi telor ayam Rp 10.000")
    st.write("12. nasi telor sosis Rp 10.000")
    st.write("13. nasi telor baso Rp 10.000")
    st.write("14. nasi goreng Rp 10.000")
    st.write("15. nasi goreng ayam Rp 11.000")
    st.write("16. nasi goreng sosis Rp 11.000")
    st.write("17. nasi goreng baso Rp 11.000")
    st.write("18. nasi goreng spesial Rp 13.000")
    st.write("19. magelangan Rp 11.000")
    st.write("20. magelangan ayam Rp 12.000")
    st.write("21. magelangan sosis Rp 12.000")
    st.write("22. magelangan baso Rp 12.000")
    st.write("23. magelangan spesial Rp 14.000")
    st.write("24. nasi orak-arik Rp 9.000")
    st.write("25. nasi orak-arik ayam Rp 10.000")
    st.write("26. nasi orak-arik sosis Rp 10.000 ")
    st.write("27. nasi orak-arik baso Rp 10.000")
    st.write("28. nasi orak-arik gorengan Rp 10.000")
    st.write("29. nasi orak-arik spesial Rp 13.000")
    st.write("30. nasi ayam bali Rp 11.000")
    st.write("31. nasi ayam bali sosis Rp 12.000")
    st.write("32. nasi ayam bali baso Rp 12.000")
    st.write("33. nasi ayam bali gorengan Rp 12.000")
    st.write("34. nasi ayam geprek Rp 12.000")
    st.write("35. nasi telur geprek Rp 10.000")

    st.subheader("GONGSO")
    st.write("1. gongso ayam Rp 11.000")
    st.write("2. gongso sosis Rp 10.000")
    st.write("3. gongso baso Rp 10.000")
    st.write("4. gongso special Rp 14.000")


    st.header("Pilihan Menu Minuman:")
    st.write("1. Es teh/panas Rp 3.000")
    st.write("2. Es syrup Rp 4.000")
    st.write("3. Es soda gembira Rp 10.000")
    st.write("4. Es susu syrup Rp 5.000")
    st.write("5. Es x- joss susu Rp 7.000")
    st.write("6. Es kukubima Rp 3.000")
    st.write("7. Es kopi hitam Rp 3.000")
    st.write("8. Es susu Rp 4.000")
    st.write("9. Es capucino Rp 4.000")
    st.write("10. Es beng-beng Rp 4.000")
    st.write("11. Es chocolatos Rp 4.000")
    st.write("12. Es gooday freeze Rp 4.000")
    st.write("13. Es gooday Rp 3000")
    st.write("14. Es nutri sari Rp 3.000")
    st.write("15. Es milo Rp 4.000")
    st.write("16. Es zee Rp 5.000")
    st.write("17. Es dancow Rp 6.000")
    st.write("18. Es hilo Rp 4.000")
    st.write("19. Es abc Rp 3.000")
    st.write("20. Es energen Rp 4.000")
    st.write("22. Es susu jahe Rp 3.000")
    st.write("23. Es x-joss Rp 3.000")

if "Menu_Pilihan" == 1:
    st.writer('mie tante dengan harga Rp 7.000')
    Jumlah = st.number_input("Jumlah Pesanan", 0)
    Total = (Jumlah * 7000)
    st.write("Total Harga = Rp ", Total)

elif "Menu_Pilihan" == 2:
    st.write('mie telor dengan harga Rp 10.000')
    Jumlah = st.number_input("Jumlah Pesanan", 0)
    Total = (Jumlah * 10000)
    st.write("Total Harga = Rp ", Total)

elif "Menu_Pilihan" == 3:
    st.writer('mie dok-dok dengan harga Rp 11.000')
    Jumlah = st.number_input("Jumlah Pesanan", 0)
    Total = (Jumlah * 11000 )
    st.write("Total Harga = Rp ", Total)

elif "Menu_Pilihan" == 4:
    st.writer('mie dok-dok ayam dengan harga Rp 12.000')
    Jumlah = st.number_input("Jumlah Pesanan", 0)
    Total = (Jumlah * 12000 )
    st.write("Total Harga = Rp ", Total)

elif "Menu_Pilihan" == 5:
    st.writer('mie dok-dok sosis dengan Rp 12.000')
    Jumlah = st.number_input("Jumlah Pesanan", 0)
    Total = (Jumlah * 12000 )
    st.write("Total Harga = Rp ", Total)

elif "Menu_Pilihan" == 6:
    st.writer('mie dok-dok baso dengan harga Rp 12.000')
    Jumlah = st.number_input("Jumlah Pesanan", 0)
    Total = (Jumlah * 12000 )
    st.write("Total Harga = Rp ", Total)

elif "Menu_Pilihan" == 7:
    st.writer('mie dok-dok special dengan harga Rp 14.000')
    Jumlah = st.number_input("Jumlah Pesanan", 0)
    Total = (Jumlah * 14000 )
    st.write("Total Harga = Rp ", Total)

elif "Menu_Pilihan" == 8:
    st.writer('mie spesial dengan harga Rp 11.000')
    Jumlah = st.number_input("Jumlah Pesanan", 0)
    Total = (Jumlah * 11000 )
    st.write("Total Harga = Rp ", Total)

elif "Menu_Pilihan" == 9:
    st.writer('mie spesial ayam dengan harga Rp 12.000')
    Jumlah = st.number_input("Jumlah Pesanan", 0)
    Total = (Jumlah * 12000 )
    st.write("Total Harga = Rp ", Total)

elif "Menu_Pilihan" == 10:
    st.writer('mie spesial sosis dengan harga Rp 12.000')
    Jumlah = st.number_input("Jumlah Pesanan", 0)
    Total = (Jumlah * 12000 )
    st.write("Total Harga = Rp ", Total)

elif "Menu_Pilihan" == 11:
    st.writer('mie spesial baso dengan harga Rp 12.000')
    Jumlah = st.number_input("Jumlah Pesanan", 0)
    Total = (Jumlah * 12000 )
    st.write("Total Harga = Rp ", Total)

if test == 'Pemesanan':
    st.text_input("Nama Pelanggan")
    st.number_input("No Meja", 0, 10)
    test1 = st.text_area("Masukan Pesanan","")
    st.write('pesanan yang masuk:',test1)
    st.info("Konfirmasi Pesanan")
    if (st.button("Yes")):
        st.text("pesanan telah masuk")

    st.write("========================================================================================")
    st.write("TERIMA KASIH TELAH MEMESAN")
    st.write("========================================================================================")