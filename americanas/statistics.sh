#!/bin/bash

NUMBER_OF_REQUESTS=`cat batch.out | grep 'Getting price' | wc -l`
NUMBER_OF_PRICES=`cat batch.out | grep -ER '[0-9]+\.[0-9]+$' | wc -l`
NUMBER_OF_SUCCESSES=`perl -e "print $NUMBER_OF_PRICES/$NUMBER_OF_REQUESTS"`

echo "Number of requests: $NUMBER_OF_REQUESTS"
echo "Number of prices got: $NUMBER_OF_PRICES"
echo "Percentage of possibly successes: $NUMBER_OF_SUCCESSES"
