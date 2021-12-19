from pyfiglet import Figlet
import argparse
import ast
import json
from voice_biometric.create_dataset import _run_new_dataset
# --------------------


# Command Header
def _run_command(production):
    _production = ast.literal_eval(production)
    # membuat block header besar 
    f = Figlet(font='standard',width=200)
    print(f.renderText('Angeline Artificial'))
    
    if not _production:
        # print ucapan selamat datang
        print('Selamat datang di Angeline Artificial 😜 \n\n')
        _run()
    else:
        return
        
# ----------------
# method informasi
def _info(*args):
    print("Angeline adalah project assistent pintar yang memiliki misi untuk membantu \n"
                 + "aktivitas manusia dimasa depan, Machine learning angeline akan dibangun dengan kosep API, \n"
                 + "dimana semua request dari perangkat IOT akan memanggil tiap-tiap kecerdasan yang tersedia")

# method untuk membuat dataset baru
def _dataset(*args):
    # membaca directory model audio dari config.json
    _config = open('./config.json')
    # load file json
    _config = json.load(_config)
    # mendapatkan lokasi directori audio
    _directory_audio = _config['angeline']['model']['audio_training_dir']
    # mendapatkan lokasi directori dataset
    _directory_dataset = _config['angeline']['dataset']['voice']
    _run_new_dataset(_directory_dataset,_directory_audio)
    

def _run():
    parse = argparse.ArgumentParser()
    
    parse.add_argument('-i','--info', action='store_true', help="Informasi lengkap Angeline")
    parse.add_argument('-nd','--new-dataset', action='store_true', help="Membuat dataset baru")
    parse.add_argument('-rm','--run-model', help="Melihat model")
    
    args = parse.parse_args()
    
    
    if args.info:
        _info(args)
    elif args.new_dataset:
        _dataset(args)
    else:
        output = input('memulai menjalankan Angeline ? ')
        return output


if __name__ == "__main__":
    _run_command("False")