list_user = [{
    "id": "CT007",
    "full_name": "Nguyen Quang Hai",
    "number_round": 1,
    "score": 1,
    "duong_kien_tao": 1,
    "diem_hieu_xuat": 9,
    "phong_do": "Cần thanh lý/ Cho mượn"
}]

def menu():
    return input('''
        1 Hiển thị danh sách cầu thủ
        2 Tiếp nhận cầu thủ mới
        3 Cập nhật thông tin và chỉ số
        4 Xóa cầu thủ (Thanh lý hợp đồng)
        5 Tìm kiếm cầu thủ
        6 Thống kê phân loại phong độ
        7 Thoát chương trình
                 
        Nhập lựa chọn của bạn: ''')

def display_user(list_user):
    print("Mã   | Tên    | Số trận đấu  | Số bàn thắng | Đường kiến tạo | Điểm hiệu xuất | Phong độ")
    for value in list_user:
        print(f"{value['id']} | {value['full_name']} | {value['number_round']} | {value['score']} | {value['duong_kien_tao']} | {value['diem_hieu_xuat']} | {value['phong_do']}")

def tinh_hieu_xuat(new_number_round, new_score, new_duong_kien_tao):
    diem_hieu_xuat = (new_number_round*1 + new_score*3 + new_duong_kien_tao*2)
    if diem_hieu_xuat < 15:
        phong_do = "Cần thanh lý/ Cho mượn"
    elif diem_hieu_xuat < 30:
        phong_do = "Dữ bị chiến lược"
    elif diem_hieu_xuat < 50:
        phong_do = "Trụ cột đội bóng"
    elif diem_hieu_xuat >= 50:
        phong_do = "Ngôi sao đẳng cấp"
    return diem_hieu_xuat, phong_do

def check_id():
    while True:
        input_id = input("Hãy nhập mã cầu thủ: ").strip().upper()
        if not input_id:
            print("Mã cầu thủ không được để trống")
            continue
        break
    for value in list_user:
        if value[0] == input_id:
            return value, input_id
    return {}, input_id

def check_int(do):
    while True:
        new_input = input(f"Hãy nhập số {do}: ").strip()
        if not new_input:
            print(f"Số {do} không được để trống")
            continue
        if not new_input.isdigit():
            print("Hãy nhập số tự nhiên")
            continue
        return int(new_input)

def uppdate_user():
    new_user = check_id()[0]
    if not new_user:
        print("Không tồn tại ID này")
        return
    new_user['number_round'] = check_int("trận đấu")
    new_user['score'] = check_id("bàn thắng")
    new_user['duong_kien_tao'] = check_id("đường kiến tạo")
    
    new_user['diem_hieu_xuat'], new_user['phong_do'] = tinh_hieu_xuat(new_user['number_round'], new_user['score'], new_user['duong_kien_tao'])
    print('Cập nhật cầu thủ thành công')

def delete_user():
    new_user = check_id()[0]
    if not new_user:
        print("Mã cầu thủ không tồn tại")
        return
    while True:
        confirm = input("Bạn có chắc muốn xóa cầu thủ này khỏi hệ thống không (Y/N): ").strip().lower()
        if confirm == "y":
            list_user.remove(new_user)
            return
        elif confirm == "n":
            print("Hủy thao tác xóa")
            return
        else:
            print("Dữ liệu không hợp lệ")
    
def add_user():
    new_user, new_id = check_id()
    if new_user:
        print("Mã cầu thủ đã tồn tại")
        return
    new_user['id'] = new_id
    while True:
        new_name = input("Hãy nhập tên cầu thủ: ").strip().title()
        if not new_name:
            print("Tên cầu thủ không được để trống")
            continue
        new_user['full_name'] = new_name
        break
    new_user['number_round'] = check_int("trận đấu")
    new_user['score'] = check_id("bàn thắng")
    new_user['duong_kien_tao'] = check_id("đường kiến tạo")

    new_user['diem_hieu_xuat'], new_user['phong_do'] = tinh_hieu_xuat(new_user['number_round'], new_user['score'], new_user['duong_kien_tao'])
    list_user.append(new_user)
    print("Thêm cầu thủ thành công")

def thong_ke():
    thanh_ly = 0
    chien_luoc = 0
    tru_cot = 0
    ngoi_sao = 0
    for value in list_user:
        if value[5] < 15:
            thanh_ly += 1
        elif value[5] < 30:
            chien_luoc += 1
        elif value[5] < 50:
            tru_cot += 1
        elif value[5] >= 50:
            ngoi_sao += 1
    print(f"Số ngôi sao: {ngoi_sao}")
    print(f"Số ngôi sao: {tru_cot}")
    print(f"Số ngôi sao: {chien_luoc}")
    print(f"Số ngôi sao: {thanh_ly}")

def find_phong_do():
    choice_find = input('''
                Bạn muốn tìm kiếm theo phương thức nào ?
                1. Mã 
                2. Tên
                Hãy nhập lựa chọn của bạn: ''')
    if choice_find == '1':
        find_user = check_id()[0]
        if not find_user:
            print("không tồn tại cầu thủ trên")
            return
        display_user([find_user])
    elif choice_find == '2':
        find_name = input("Hãy nhập tên bạn muốn tìm kiếm: ").strip().lower()
        for value in list_user:
            if value['full_name'] in find_name.split():
                

def main():
    while True:
        choice = menu()
        if choice.isdigit():
            choice = int(choice)
            match choice:
                case 1:
                    display_user(list_user)
                case 2:
                    add_user()
                case 3:
                    uppdate_user()
                case 4:
                    delete_user()
                case 5: 
                case 6:
                    thong_ke()
                case 7:
                    print("Kết thúc chương trình")
                    break
                case _:
                    print("Dữ liệu không hợp lệ")
        print("Dữ liệu không hợp lệ")