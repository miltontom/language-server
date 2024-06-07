# Toy Language Server

This is a toy project that I'm building from scratch without any external dependencies and only using python's stdlib.

## Motivation

My curiosity about how code completion and other language support features work in code editors like VS Code and Neovim led me to build my own language server from scratch as a learning experience and to improve my skills as a developer.

## Goal
In the longrun my goal is to build a language server,  

* **for**: LÖVE 2D framework  
* **with**: Python  
* **over**: STDIO  
* **supporting:** code completion  
* **for client**: Neovim  

## Progress

* [x] Handle initialization
* [ ] Handle basic server lifecycle messages  
. . .

## Setup
Setting up the server with Neovim is really easy, inside Neovim's config folder create a 
file `init.lua` and add this config.
```lua
local client = vim.lsp.start_client({
	name = "your language server name",
	cmd = {"python", "path\\to\\script.py"} -- escape the '\' (for Windows)
})

if not client then
	vim.notify("Couldn't setup the client.")
	return 
end

-- the server will be attached with markdown files, specify the type you want to work with
vim.api.nvim_create_autocmd(
    "FileType",
    {pattern="markdown", callback=function() vim.lsp.buf_attach_client(0, client) end}
)
```
When you open a markdown file, you can check if the server is actually up by executing `checkhealth lsp` in `COMMAND` mode (press `:` in `NORMAL` mode)

## Helpful Resources

* [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) specification.
* [JSON-RPC](https://www.jsonrpc.org/) specification.
* **TJ DeVries's** "LSP from scratch" [video](https://youtu.be/YsdlcQoHqPY?feature=shared) (Go implementation).
