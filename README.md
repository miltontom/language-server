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

## Helpful Resources

* [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) specification.
* [JSON-RPC](https://www.jsonrpc.org/) specification.
* **TJ DeVries's** "LSP from scratch" [video](https://youtu.be/YsdlcQoHqPY?feature=shared) (Go implementation).
