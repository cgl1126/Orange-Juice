#!/bin/bash

g_filePath=$(dirname $(pwd))/$(basename $0)

# g_dateTime=$(date "+%Y%m%d_%H%M%S")

# get current time
function log_get_time_stamp(){
    local date=$(date "+%Y%m%d_%H%M%S")
    echo "${date}"
}

function log_echo(){
    local echoMsg=$1
    local colorNo=$2

    echo -e "\033[${colorNo}m${echoMsg}\033[0m"
}

# log print format
function log_msg_handle(){
    local logLevel=$1   
    local fileName=$2
    local logMsg=$3
    local colorNo=$4
    local dateTime=$(log_get_time_stamp)

    log_echo "[""${dateTime}""]\c" "0"
    log_echo "[""${logLevel}""]\c" "0"
    log_echo "[""${fileName}""]\c" "0"
    log_echo "${logMsg}" "${colorNo}"

}


function log_info(){
    local fileName=$1
    local logMsg=$2
    local colorNo=0

    log_msg_handle "INFO" "${fileName}" "${logMsg}" "${colorNo}"
}


function log_info_color(){
    local fileName=$1
    local logMsg=$2
    local colorNo="44;37"

    log_msg_handle "INFO" "${fileName}" "${logMsg}" "${colorNo}"
}


function log_error(){
    local fileName=$1
    local logMsg=$2
    local colorNo="41;37"

    log_msg_handle "ERROR" "${fileName}" "${logMsg}" "${colorNo}"
}


function log_succ(){
    local fileName=$1
    local logMsg=$2
    local colorNo="42;37"

    log_msg_handle "^_^" "${fileName}" "${logMsg}" "${colorNo}"
}


function main(){
    log_info ${g_filePath} "INFO This is test info"
    log_info_color ${g_filePath} "INFO This is test info"
    log_error ${g_filePath} "ERROR This is test info This is test info This is test info This is test info This is test info"
    log_succ ${g_filePath} "SUCC This is test info"
}

main
