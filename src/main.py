import ocr
import sldata
import analysis

# Path variable
img_path = "../data/img/screen.png"

if __name__ == "__main__":
    #df = ocr.ocr_dataframe(img_path)

    #sldata.save_to_csv(df)
    
    df = sldata.import_csv()
    print(df)
