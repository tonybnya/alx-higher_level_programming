#!/usr/bin/python3
if __name__ == "__main__":
    def element_at(my_list, idx):
        if idx < 0 and idx > len(my_list):
            return None

        return (my_list[idx])
