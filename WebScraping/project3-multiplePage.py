from bs4 import BeautifulSoup
import requests
import pandas as pd
Name = []
Price = []
Description = []
Rating = []

url = 'https://www.airbnb.com/s/New-Delhi--Delhi--India/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-01-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&query=New%20Delhi%2C%20Delhi%2C%20India&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&price_filter_num_nights=5&federated_search_session_id=73c5dfeb-b720-4a50-8666-cea098d196d0&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MCwiaXRlbXNfb2Zmc2V0IjowLCJ2ZXJzaW9uIjoxfQ%3D%3D'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print(r)
for i in range(1, 6):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    np = soup.find('a', class_='l1ovpqvx atm_1y33qqm_1ggndnn_10saat9 atm_17zvjtw_zk357r_10saat9 atm_w3cb4q_il40rs_10saat9 c1ytbx3a atm_mk_h2mmj6 atm_9s_1txwivl atm_h_1h6ojuz atm_fc_1h6ojuz atm_bb_idpfg4 atm_26_1j28jx2 atm_3f_glywfm atm_7l_18pqv07 atm_gi_idpfg4 atm_l8_idpfg4 atm_uc_1dtz4sb atm_kd_glywfm atm_gz_xvenqj atm_uc_glywfm__p88qr9 atm_26_1nh1gcj_1rqz0hn_uv4tnr atm_tr_kv3y6q_csw3t1 atm_26_1nh1gcj_1ul2smo atm_3f_glywfm_jo46a5 atm_l8_idpfg4_jo46a5 atm_gi_idpfg4_jo46a5 atm_3f_glywfm_1icshfk atm_kd_glywfm_19774hq atm_70_glywfm_1w3cfyq atm_uc_x37zl0_9xuho3 atm_70_216vci_9xuho3 atm_26_1nh1gcj_9xuho3 atm_uc_glywfm_9xuho3_p88qr9 atm_70_glywfm_18zk5v0 atm_uc_x37zl0_fiqcvf atm_70_216vci_fiqcvf atm_26_1nh1gcj_fiqcvf atm_uc_glywfm_fiqcvf_p88qr9 atm_7l_161hw1_1o5j5ji atm_9j_13gfvf7_1o5j5ji atm_26_1j28jx2_154oz7f atm_92_1yyfdc7_vmtskl atm_9s_1ulexfb_vmtskl atm_mk_stnw88_vmtskl atm_tk_1ssbidh_vmtskl atm_fq_1ssbidh_vmtskl atm_tr_pryxvc_vmtskl atm_vy_1vi7ecw_vmtskl atm_e2_1vi7ecw_vmtskl atm_5j_1ssbidh_vmtskl atm_mk_h2mmj6_1ko0jae dir dir-ltr').get("href")
    cnp = "https://www.airbnb.com"+str(np)
    url = cnp
    r = requests.get(url)

    # soup = BeautifulSoup(r.text, 'html.parser')
    box = soup.find('div', class_="gsgwcjk atm_10yczz8_kb7nvz atm_10yczz8_cs5v99__1ldigyt atm_10yczz8_11wpgbn__1v156lz atm_10yczz8_egatvm__qky54b atm_10yczz8_qfx8er__1xolj55 atm_10yczz8_ouytup__w5e62l g8ge8f1 atm_1d13e1y_k75hcd atm_yrukzc_wwb3ei atm_10yczz8_cs5v99_vagkz0_1ldigyt atm_10yczz8_11wpgbn_vagkz0_1h2hqoz g14v8520 atm_9s_11p5wf0 atm_d5_j5tqy atm_d7_1ymvx20 atm_dl_1mvrszh atm_dz_hxz02 dir dir-ltr")

    names = box.find_all(
        'div', class_='t1jojoys atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_1vgr820 atm_7l_18pqv07 atm_cs_qo5vgd atm_w4_1eetg7c atm_ks_zryt35__1rgatj2 dir dir-ltr')
    print(len(names))

    for i in names:
        name = i.text
        if name is not None:

            Name.append(name)
        else:
            Name.append(0)

    prices = box.find_all('div', class_='_i5duul')
    print(len(prices))
    for i in prices:
        price = i.text
        if price is not None:

            Price.append(price)
        else:
            Price.append(0)

    desc = box.find_all(
        'span', class_='t6mzqp7 atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_kb7nvz atm_7l_12u4tyr atm_am_qk3dho atm_ks_zryt35__1rgatj2 dir dir-ltr')
    print(len(desc))
    for i in desc:
        des = i.text
        if des is not None:
            Description.append(des)
        else:
            Description.append(0)

    rating = box.find_all(
        'span', class_='r1dxllyb atm_7l_18pqv07 atm_cp_1ts48j8 dir dir-ltr')
    print(len(rating))
    for i in rating:
        rate = i.text
        if rate is not None:
            Rating.append(rate)
        else:
            Rating.append(0)

df = pd.DataFrame({"names": Name, "Prices": Price,
                  "Description": Description, "Rating": Rating})
df.to_excel("project3_hotel_airbnb.xlsx")
