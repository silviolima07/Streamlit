mkdir -p ~/.streamlit/


echo "config.toml"
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

echo "credencial.toml"
echo "\
[general]\n\
email = \"silcesarlima@yahoo.com.br\"\n\
" > ~/.streamlit/credentials.toml


echo "PORTA USADA:" $PORT
echo "enableCORS:"$enableCORS
