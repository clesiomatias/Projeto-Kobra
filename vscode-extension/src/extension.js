const vscode = require('vscode');
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

        // Usar apenas terminal integrado para interação completa
        const terminal = vscode.window.createTerminal({
            name: 'Kobra',
            cwd: cwd
        });
        terminal.show();
        terminal.sendText(`python3 kobra.py "${path.basename(filePath)}"`);
        
        vscode.window.showInformationMessage(`Executando ${path.basename(filePath)} no terminal...`);
    });

    context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};