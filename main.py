from source import GetImageData


def main():
    image_data = GetImageData.get_image()
    image_data[0].save(f"output/{image_data[1]}.jpg")

if __name__ == "__main__":
    main()