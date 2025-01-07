import pickle
import streamlit as st

with st.sidebar:
   add_selectbox = st.sidebar.selectbox(
       "Apa yang mau anda prediksi?",
       ("Status Depresi", "Cuaca", "Penyakit Jantung")
   )

if (add_selectbox == "Status Depresi"):
   model = pickle.load(open('model.pkl', 'rb'))
   
   st.title('Prediksi Depresi')
   
   col1, col2, col3 = st.columns(3)
   with col1:
      Jeniskelamin = st.selectbox('Masukan Jenis Kelamin',["Pria","Perempuan"])
      if Jeniskelamin == "Pria":
         Jeniskelamin = 1
      else:
         Jeniskelamin = 0
         
      DurasiTidur = st.selectbox('Masukan Durasi Tidur',["Kurang dari 5 jam","5-6 jam","7-8 jam","Lebih dari 8 jam"])
      if DurasiTidur == "5-6 jam":
         DurasiTidur = 0
      elif DurasiTidur == "7-8 jam": 
           DurasiTidur = 1
      elif DurasiTidur == "Kurang dari 5 jam": 
           DurasiTidur = 2
      else :
         DurasiTidur = 3
   
      KebiasaanDiet = st.selectbox('Masukan Kebiasaan Diet',["Tidak Sehat","Sedang","Sehat"])
      if KebiasaanDiet == "Tidak Sehat":
         KebiasaanDiet = 2
      elif KebiasaanDiet == "Sedang": 
           KebiasaanDiet = 0
      else :
         KebiasaanDiet = 1
   
      PernahkahAnda = st.selectbox('Pernahkah Anda Memiliki Perasaan Untuk Bunuh Diri?',["Tidak","Ya"])
      if PernahkahAnda == "Tidak":
          PernahkahAnda = 0
      else:
          PernahkahAnda = 1
   
      RiwayatKeluarga = st.selectbox('Riwayat Keluarga dengan Penyakit Mental',["Tidak","Ya"])
      if RiwayatKeluarga == "Tidak":
          RiwayatKeluarga = 0
      else:
          RiwayatKeluarga = 1     
    
   with col2:
      Usia = st.slider('Masukan Usia',18,35)   
   
      JamBelajar	= st.slider('Masukan Jam Belajar',1,12)
   
      TekananAkademis	= st.select_slider('Masukan Tekanan Akademis',["Sangat Tidak Tertekan","Tidak Tertekan","Cukup Tertekan","Tertekan","Sangat Tertekan"])
      if TekananAkademis == "Sangat Tertekan":
         TekananAkademis = 5
      elif TekananAkademis == "Tertekan": 
           TekananAkademis = 4
      elif TekananAkademis == "Cukup Tertekan": 
           TekananAkademis = 3
      elif TekananAkademis == "Tidak Tertekan": 
           TekananAkademis = 2
      else :
         TekananAkademis = 1 
   
      KepuasanBelajar = st.select_slider('Masukan Kepuasan Belajar',["Sangat Tidak Puas","Tidak Puas","Cukup Puas","Puas","Sangat Puas"])
      if KepuasanBelajar == "Sangat Puas":
         KepuasanBelajar = 5
      elif KepuasanBelajar == "Puas": 
           KepuasanBelajar = 4
      elif KepuasanBelajar == "Cukup Puas": 
           KepuasanBelajar = 3
      elif KepuasanBelajar == "Tidak Puas": 
           KepuasanBelajar = 2
      else :
         KepuasanBelajar = 1 
   
      StresKeuangan	= st.select_slider('Masukan Stres Keuangan',["Sangat Tidak Stres","Tidak Stres","Cukup Stres","Stres","Sangat Stres"])
      if StresKeuangan == "Sangat Stres":
         StresKeuangan = 5
      elif StresKeuangan == "Stres": 
           StresKeuangan = 4
      elif StresKeuangan == "Cukup Stres": 
           StresKeuangan = 3
      elif StresKeuangan == "Tidak Stres": 
           StresKeuangan = 2
      else :
         StresKeuangan = 1
   
      predict = ''
      
   with col3:
      if st.button('Proses'):
          predict = model.predict(
              [[Jeniskelamin, Usia, TekananAkademis, KepuasanBelajar, DurasiTidur, KebiasaanDiet, PernahkahAnda, JamBelajar, StresKeuangan, RiwayatKeluarga]]
          )
          if predict == "Ya":         
            st.warning('Status Mengalami Depresi', icon="⚠️")
            st.toast('Segera Konsultasi ke Dokter!', icon='🚨')
          else :
            st.success('Status Tidak Mengalami Depresi', icon="✅")
            st.toast('Tetap Jaga Kesehatan!', icon='😍')
            st.snow()
             
elif (add_selectbox == "Cuaca"):
   st.title('Haerul blm merancang model Cuaca')
else :
   st.title('Haerul blm merancang model Penyakit')
