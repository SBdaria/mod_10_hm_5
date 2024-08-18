from datetime import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':
    file_names = [f'./file {i}.txt' for i in range(1, 5)]
    start_lin = datetime.now()
    for i in file_names:
        read_info(i)
    end_lin = datetime.now()
    print(end_lin - start_lin)

    start_pro = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    end_pro = datetime.now()
    print(end_pro - start_pro)
