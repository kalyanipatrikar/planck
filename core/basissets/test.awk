#!/usr/bin/awk -f

BEGIN {
    RS = "\n"
    file_counter = 1
    output_file = "3-21g-" file_counter ".txt"
}

{
    if ($0 == "****") {
        close(output_file)
        file_counter++
        output_file = "3-21g-" file_counter ".txt"
    } else {
        print $0 >> output_file
    }
}
