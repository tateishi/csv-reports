#! /usr/bin/bash

HEADER="date,payee,account,amount,note,file,line,parent_id"
FILE=~/wks/ledger/ledger_kakei/main.ledger
OUT=~/wks/data/csv/main_kakei.csv

ledger csv \
        --csv-format "%(quoted(date)),%(quoted(payee)),%(quoted(account)),%(quoted(amount)),%(quoted(note)),%(quoted(filename)),%(quoted(beg_line)),%(quoted(parent.id))\n" \
        --file ${FILE} | sed -e "1i${HEADER}" > ${OUT}
