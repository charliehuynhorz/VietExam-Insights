import pandas as pd

input_file = 'data/raw/raw_national_exam_scores_2025.csv'
output_file = 'data/processed/viet_national_exam_scores.csv'

df = pd.read_csv(input_file, dtype={'SBD': str})

rename_dict = {
    'SBD': 'Số báo danh',
    'TOAN': 'Toán',
    'VAN': 'Ngữ văn',
    'NGOAI_NGU': 'Ngoại ngữ',
    'LI': 'Vật lý',
    'HOA': 'Hóa học',
    'SINH': 'Sinh học',
    'SU': 'Lịch sử',
    'DIA': 'Địa lý',
    'TIN_HOC': 'Tin học',
    'CN_CONG_NGHIEP': 'CN Công nghiệp',
    'CN_NONG_NGHIEP': 'CN Nông nghiệp',
    'GDKT_PL': 'GD Kinh tế và Pháp luật',
    'TONGDIEM': 'Tổng điểm'
}
df.rename(columns=rename_dict, inplace=True)

province_map = {
    '01': 'HÀ NỘI',
    '02': 'HỒ CHÍ MINH',
    '03': 'HẢI PHÒNG',
    '04': 'ĐÀ NẴNG',
    '05': 'HÀ GIANG',
    '06': 'CAO BẰNG',
    '07': 'LAI CHÂU',
    '08': 'LÀO CAI',
    '09': 'TUYÊN QUANG',
    '10': 'LẠNG SƠN',
    '11': 'BẮC KẠN',
    '12': 'THÁI NGUYÊN',
    '13': 'YÊN BÁI',
    '14': 'SƠN LA',
    '15': 'PHÚ THỌ',
    '16': 'VĨNH PHÚC',
    '17': 'QUẢNG NINH',
    '18': 'BẮC GIANG',
    '19': 'BẮC NINH',
    '21': 'HẢI DƯƠNG',
    '22': 'HƯNG YÊN',
    '23': 'HÒA BÌNH',
    '24': 'HÀ NAM',
    '25': 'NAM ĐỊNH',
    '26': 'THÁI BÌNH',
    '27': 'NINH BÌNH',
    '28': 'THANH HÓA',
    '29': 'NGHỆ AN',
    '30': 'HÀ TĨNH',
    '31': 'QUẢNG BÌNH',
    '32': 'QUẢNG TRỊ',
    '33': 'THỪA THIÊN - HUẾ',
    '34': 'QUẢNG NAM',
    '35': 'QUẢNG NGÃI',
    '36': 'KON TUM',
    '37': 'BÌNH ĐỊNH',
    '38': 'GIA LAI',
    '39': 'PHÚ YÊN',
    '40': 'ĐẮK LẮK',
    '41': 'KHÁNH HÒA',
    '42': 'LÂM ĐỒNG',
    '43': 'BÌNH PHƯỚC',
    '44': 'BÌNH DƯƠNG',
    '45': 'NINH THUẬN',
    '46': 'TÂY NINH',
    '47': 'BÌNH THUẬN',
    '48': 'ĐỒNG NAI',
    '49': 'LONG AN',
    '50': 'ĐỒNG THÁP',
    '51': 'AN GIANG',
    '52': 'BÀ RỊA – VŨNG TÀU',
    '53': 'TIỀN GIANG',
    '54': 'KIÊN GIANG',
    '55': 'THÀNH PHỐ CẦN THƠ',
    '56': 'BẾN TRE',
    '57': 'VĨNH LONG',
    '58': 'TRÀ VINH',
    '59': 'SÓC TRĂNG',
    '60': 'BẠC LIÊU',
    '61': 'CÀ MAU',
    '62': 'ĐIỆN BIÊN',
    '63': 'ĐĂK NÔNG',
    '64': 'HẬU GIANG'
}

df.insert(1, 'Mã tỉnh', df['Số báo danh'].astype(str).str[:2])

df['Mã tỉnh'] = df['Mã tỉnh'].map(province_map).fillna('Không rõ')

df.to_csv(output_file, index=False, encoding='utf-8-sig')

print("Processed")
