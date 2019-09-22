function write_report {
    echo -ne $1 > /dev/hidg0
}

# H (press shift and H)
write_report "\x05\0\x17\0\0\0\0\0"

# Release al keys
write_report "\0\0\0\0\0\0\0\0"
