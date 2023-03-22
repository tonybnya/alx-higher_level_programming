#!/bin/bash

read -rp "filename: " filename
touch "$filename"

echo "#!/usr/bin/python3" >> "$filename"
echo "# $filename" >> "$filename"
echo "# Author: @tonybnya" >> "$filename"
echo '"""' >> "$filename"
echo "This script" >> "$filename"
echo '"""' >> "$filename"

echo "" >> "$filename"
echo "" >> "$filename"

echo "if __name__ == '__main__':" >> "$filename"
echo "    main()" >> "$filename"

chmod u+x "$filename"
vim "$filename"
