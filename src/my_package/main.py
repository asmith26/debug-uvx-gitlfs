from pathlib import Path


def main():
    print("Hello my_package!")

def main_gitlfs():
    with (Path(__file__).parent / "git-lfs.txt").open("r") as f:
        print(f.read())  # Should print "Hello my_package_gitlfs!"


if __name__ == "__main__":
    main()
