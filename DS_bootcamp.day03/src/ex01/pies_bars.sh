#!/bin/bash

DATA=$(
cat <<EOF
2007 73.32 70.52
2008 81.23 93.00
2009 181.43 135.10
2010 110.21 95.00
2011 93.97 90.45
EOF
)

echo -e "\033[1;35m▇\033[0m \033[1;35mPies\033[0m  \033[1;36m▇\033[0m \033[1;36mBars\033[0m"  
echo ""

echo "$DATA" | termgraph --color magenta cyan --width 40
