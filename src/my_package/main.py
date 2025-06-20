def main():
    print("Hello my_package!")

def main_gitlfs():
    with open("git-lfs.txt", "r") as f:
        print(f.read())  # Should print "Hello my_package_gitlfs!"


if __name__ == "__main__":
    main()
