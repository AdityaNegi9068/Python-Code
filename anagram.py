def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

def main():
    s = input("Enter string s: ")
    t = input("Enter string t: ")
    
    if is_anagram(s, t):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()