#! php
<?php
/* regex 😍 https://regex101.com/r/iZrrbe/1 */
function alerta()
{
    echo "\nTente o seguinte:\n\t./Scripit \"diretorio-alvo\" \"extenção-do-arquivo\" \"formato-de-saida\"\n";
    echo "\tObs: Não esqueça as ASPAS.";
    echo "\n\nExemplo com MP3:\n\t./Scripit \"Documentos/Musicas\" \"mp3\" \"csv\"";
    echo "\n\nExemplo para todos os tipos de arquivo e diretórios:\n\t./Scripit \"Documentos/Downloads\" \"*\" \"json\"\n";
    die;
}
if (sizeof($argv) != 4) {
    alerta();
};
$output = shell_exec("ls {$argv[1]} -ltr --time-style='+%s' | grep \".{$argv[2]}\"");
preg_match_all("/^.*\s+(\d+)\s(\d+)\s(.*)$/m", $output, $matches, PREG_SET_ORDER, 0);

switch ($argv[3]) {
    case 'csv':
        echo "{#NOME}|{#SIZE}|{#UPTIME}";
        foreach ($matches as $key => $value) {
            $uptime = time() - $value[2];
            echo "\n{$value[3]}|{$value[1]}|{$uptime}";
        };
        break;

    case 'json':
        $ls = [];
        foreach ($matches as $key => $value) {
            array_push($ls, array(
                "{#NOME}" => $value[3],
                "{#SIZE}" => $value[2],
                "{#UPTIME}" => time() - $value[2],
            ));
        };
        echo json_encode($ls, 128, 256);
        break;

    default:
        alerta();
        break;
}
