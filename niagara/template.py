def generate_database_file(path):
    templ = """
{
        "packages": [
            {
                "pkgname": "picom",
                "arch": "picom",
                "void": "picom",
                "fedora": "picom",
                "debian": "picom",
                "gentoo": "x11-misc/picom"
                },
            {
                "pkgname": "kitty",
                "arch": "kitty",
                "void": "kitty",
                "fedora": "kitty",
                "debian": "kitty",
                "gentoo": "x11-terms/kitty"
                },
            {
                "pkgname": "alacritty",
                "arch": "alacritty",
                "void": "alacritty",
                "fedora": "alacritty",
                "debian": "",
                "gentoo": "x11-terms/alacritty"
                },
            {
                "pkgname": "neofetch",
                "arch": "neofetch",
                "void": "neofetch",
                "fedora": "neofetch",
                "debian": "neofetch",
                "gentoo": "app-misc/neofetch"
                },
            {
                "pkgname": "feh",
                "arch": "feh",
                "void": "feh",
                "fedora": "",
                "debian": "feh",
                "gentoo": "media-gfx/feh"
                },
            {
                "pkgname": "emacs",
                "arch": "emacs",
                "void": "emacs",
                "fedora": "",
                "debian": "emacs",
                "gentoo": "app-editors/emacs"
                },
            {
                "pkgname": "vim",
                "arch": "vim",
                "void": "vim",
                "fedora": "",
                "debian": "vim",
                "gentoo": "app-editors/vim"
                },
            {
                    "pkgname": "neovim",
                    "arch": "neovim",
                    "void": "neovim",
                    "fedora": "",
                    "debian": "neovim",
                    "gentoo": "app-editors/neovim"
                    },
            {
                    "pkgname": "rofi",
                    "arch": "rofi",
                    "void": "rofi",
                    "fedora": "",
                    "debian": "rofi",
                    "gentoo": "x11-misc/rofi"
                    },
            {
                    "pkgname": "flameshot",
                    "arch": "flameshot",
                    "void": "flameshot",
                    "fedora": "",
                    "debian": "flameshot",
                    "gentoo": "media-gfx/flameshot"
                    },
    {
            "pkgname": "doas",
            "arch": "opendoas",
            "void": "opendoas",
            "fedora": "opendoas",
            "debian": "",
            "gentoo": "app-admin/doas"
            },
    {
            "pkgname": "dunst",
            "arch": "dunst",
            "void": "dunst",
            "fedora": "",
            "debian": "dunst",
            "gentoo": "x11-misc/dunst"
            },
    {
            "pkgname": "firefox",
            "arch": "firefox",
            "void": "firefox",
            "fedora": "",
            "debian": "firefox",
            "gentoo": "www-client/firefox-bin"
            },
    {
            "pkgname": "ripgrep",
            "arch": "ripgrep",
            "void": "ripgrep",
            "fedora": "",
            "debian": "ripgrep",
            "gentoo": "sys-apps/ripgrep"
            },
    {
            "pkgname": "mpv",
            "arch": "mpv",
            "void": "mpv",
            "fedora": "",
            "debian": "mpv",
            "gentoo": "media-video/mpv"
            },
    {
            "pkgname": "dmenu",
            "arch": "dmenu",
            "void": "dmenu",
            "fedora": "",
            "debian": "",
            "gentoo": "x11-misc/dmenu"
            },
    {
            "pkgname": "lynx",
            "arch": "lynx",
            "void": "lynx",
            "fedora": "",
            "debian": "lynx",
            "gentoo": "www-client/lynx"
            },
    {
            "pkgname": "fzf",
            "arch": "fzf",
            "void": "fzf",
            "fedora": "",
            "debian": "fzf",
            "gentoo": "www-client/lynx"
            },
    {
            "pkgname": "bat",
            "arch": "bat",
            "void": "bat",
            "fedora": "",
            "debian": "bat",
            "gentoo": "sys-apps/bat"
            },
    {
            "pkgname": "ffmpeg",
            "arch": "ffmpeg",
            "void": "ffmpeg",
            "fedora": "",
            "debian": "ffmpeg",
            "gentoo": "media-video/ffmpeg"
            },
    {
            "pkgname": "ytdl",
            "arch": "youtube-dl",
            "void": "youtube-dl",
            "fedora": "",
            "debian": "youtube-dl",
            "gentoo": "net-misc/youtube-dl"
            },
    {
            "pkgname": "",
            "arch": "",
            "void": "",
            "fedora": "",
            "debian": "",
            "gentoo": ""
            }
    ]
}
"""
    with open(path, 'w+') as f:
        f.writelines(templ)
    f.close()


