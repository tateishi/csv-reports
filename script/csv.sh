#! /usr/bin/bash

HEADER="date,payee,account,amount,note,file,line,parent_id"
FILE=~/wks/ledger/ledger_tadatoshi/main.ledger

ledger csv \
        --csv-format "%(quoted(date)),%(quoted(payee)),%(quoted(account)),%(quoted(amount)),%(quoted(note)),%(quoted(filename)),%(quoted(beg_line)),%(quoted(parent.id))\n" \
        --file ${FILE} | sed -e "1i${HEADER}"
