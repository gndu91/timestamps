# find directory
SITEDIR=$(python -m site --user-site)

# create if it doesn't exist
mkdir -p "$SITEDIR"

# create new .pth file with our path
echo "$(pwd)" > "$SITEDIR/timestamps.pth"

# find directory
SITEDIR=$(python3 -m site --user-site)

# create if it doesn't exist
mkdir -p "$SITEDIR"

# create new .pth file with our path
echo "$(pwd)" > "$SITEDIR/timestamps.pth"



