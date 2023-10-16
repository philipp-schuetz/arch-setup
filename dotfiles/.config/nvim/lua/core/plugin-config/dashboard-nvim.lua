local conf = {}
conf.header = {
"                                        ",
"             ,@@@@@@@,                  ",
"     ,,,.   ,@@@@@@/@@,  .oo8888o.      ",
"  ,&%%&%&&%,@@@@@/@@@@@@,8888\\88/8o     ",
" ,%&\\%&&%&&%,@@@\\@@@/@@@88\\88888/88'    ",
" %&&%&%&/%&&%@@\\@@/ /@@@88888\\88888'    ",
" %&&%/ %&%%&&@@\\ V /@@' `88\\8 `/88'     ",
" `&%\\ ` /%&'    |.|        \\ '|8'       ",
"     |o|        | |         | |         ",
"     |.|        | |         | |         ",
"  \\/ ._\\//_/__/  ,\\_//__\\\\/.  \\_//__/_ ",
"                                        "
}

conf.center = {
  {
    icon = "󰈞  ",
    desc = "Find  File                              ",
    action = "Leaderf file --popup",
    key = "<Leader> f f",
  },
  {
    icon = "󰈢  ",
    desc = "Recently opened files                   ",
    action = "Leaderf mru --popup",
    key = "<Leader> f r",
  },
  {
    icon = "󰈬  ",
    desc = "Project grep                            ",
    action = "Leaderf rg --popup",
    key = "<Leader> f g",
  },
  {
    icon = "  ",
    desc = "Open Nvim config                        ",
    action = "tabnew $MYVIMRC | tcd %:p:h",
    key = "<Leader> e v",
  },
  {
    icon = "  ",
    desc = "New file                                ",
    action = "enew",
    key = "e",
  },
  {
    icon = "󰗼  ",
    desc = "Quit Nvim                               ",
    -- desc = "Quit Nvim                               ",
    action = "qa",
    key = "q",
  },
}


require("dashboard").setup {
  theme = "doom",
  shortcut_type = "number",
  config = conf
}
