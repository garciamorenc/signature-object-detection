import glob
import cv2

from XML_preprocesor import XmlPreprocessor


def run(path):
    input_path = path + "/*.*"

    # Loop reading image sequence
    for i in glob.glob(input_path):
        # image = cv2.imread(i)
        # cv2.imshow('image', image)

        cv2.namedWindow("output", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
        im = cv2.imread(i)  # Read image
        # im_show = cv2.resize(im, (960, 540))  # Resize image
        cv2.imshow("output", im)  # Show image
        cv2.waitKey(0)  # Display the image infinitely until any keypress

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Reading arguments
    # parser = ArgumentParser()
    # parser.add_argument("-images", "--images", dest="images", type=str, default=True)
    # parser.add_argument("-out", "--out", dest="out", type=str, default=True)
    #
    # args = parser.parse_args()
    #
    # run(args.images, args.out)
    one_hot = XmlPreprocessor('./dataset/tobacco_data_zhugy/Tobacc800_Groundtruth_v2.0/XMLGroundtruth_v2.0')
    run("./dataset/tobacco_data_zhugy/Tobacco800_SinglePage/SinglePageTIF")
