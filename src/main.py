import ocr
import sldata
import analysis

# Path variable
img_path = "../data/img/screen.png"


def treat_all_img():
    import utils

    files = utils.get_folder()

    for file in files:
        df = ocr.ocr_dataframe(file)
        sldata.save_to_csv(df)
        print('Df done !')

if __name__ == "__main__":
    treat_all_img()
