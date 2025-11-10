"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
const vscode = require("vscode");
const { exec } = require('child_process');
const path = require('path');
function activate(context) {
    let disposable = vscode.commands.registerCommand('kobra.run', () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('Nenhum arquivo Kobra aberto');
            return;
        }
        const document = editor.document;
        if (document.languageId !== 'kobra') {
            vscode.window.showErrorMessage('Este não é um arquivo Kobra');
            return;
        }
        const filePath = document.fileName;
        const workspaceFolder = vscode.workspace.getWorkspaceFolder(document.uri);
        const cwd = workspaceFolder ? workspaceFolder.uri.fsPath : path.dirname(filePath);
        document.save();
        const command = `python3 kobra.py "${filePath}"`;
        exec(command, { cwd }, (error, stdout, stderr) => {
            if (error) {
                vscode.window.showErrorMessage(`Erro ao executar Kobra: ${error.message}`);
                return;
            }
            if (stderr) {
                vscode.window.showErrorMessage(`Erro Kobra: ${stderr}`);
                return;
            }
            const terminal = vscode.window.createTerminal('Kobra Output');
            terminal.show();
            terminal.sendText(`echo "=== Saída do Kobra ==="`);
            terminal.sendText(`echo "${stdout}"`);
        });
    });
    context.subscriptions.push(disposable);
}
exports.activate = activate;
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map