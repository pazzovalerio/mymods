<?php

require_once 'lib/boot.php';
#require_once 'property-detailed.php';
#require_once 'config.php';



use Photobooth\Service\AssetService;
use Photobooth\Service\ProcessService;
use Photobooth\Utility\PathUtility;

$assetService = AssetService::getInstance();















if (!$config['ui']['skip_welcome']) {
    if (!is_file(PathUtility::getAbsolutePath('welcome/.skip_welcome'))) {
        header('location: ' . PathUtility::getPublicPath('welcome'));
        exit();
    }
}

if ($config['chromaCapture']['enabled']) {
    header('location: ' . PathUtility::getPublicPath('chroma'));
    exit();
}

// Login / Authentication check
if (
    !$config['login']['enabled'] ||
    (!$config['protect']['localhost_index'] && (isset($_SERVER['SERVER_ADDR']) && $_SERVER['REMOTE_ADDR'] === $_SERVER['SERVER_ADDR'])) ||
    ((isset($_SESSION['auth']) && $_SESSION['auth'] === true) || !$config['protect']['index'])
) {
    $pageTitle = $config['ui']['branding'];
    $photoswipe = true;
    $randomImage = false;
    $remoteBuzzer = true;
} else {
    header('location: ' . $config['protect']['index_redirect']);
    exit();
}

include PathUtility::getAbsolutePath('template/components/main.head.php');
?>

<body class="gallery-mode--overlay ">








<?php include PathUtility::getAbsolutePath('template/components/preview.php'); ?>

<?php if ($config['video']['enabled'] && $config['video']['animation']): ?>
    <div id="videoAnimation">
        <ul class="left">
            <?php for ($i = 1; $i <= 50; $i++) {
                print '<li class="reel-item"></li>';
            } ?>
        </ul>
        <ul class="right">
            <?php for ($i = 1; $i <= 50; $i++) {
                print '<li class="reel-item"></li>';
            } ?>
        </ul>
    </div>
<?php endif; ?>
<?php

include PathUtility::getAbsolutePath('template/components/stage.start.php');
include PathUtility::getAbsolutePath('template/components/stage.loader.php');
include PathUtility::getAbsolutePath('template/components/stage.results.php');

if ($config['gallery']['enabled']) {
    include PathUtility::getAbsolutePath('template/components/gallery.php');
}

if ($config['filters']['enabled']) {
    include PathUtility::getAbsolutePath('template/components/filter.php');
}

include PathUtility::getAbsolutePath('template/components/main.footer.php');

?>

<script src="<?=$assetService->getUrl('resources/js/preview.js')?>"></script>
<script src="<?=$assetService->getUrl('resources/js/core.js')?>"></script>

<?php include PathUtility::getAbsolutePath('template/components/start.adminshortcut.php'); ?>
<?php ProcessService::getInstance()->boot(); ?>














<style>
            .blink {
                animation: blinker 1.5s linear infinite;
                color: yellow;
                font-family: sans-serif;
                font-size: 32px;
                font-weight: bold;
                
            }
            .my {
                color: white;
                font-family: sans-serif;
                font-size: 32px;
                font-weight: bold;
                
            }
            @keyframes blinker {
                50% {
                    opacity: 0;
                }
            }
</style>
<html>
<head>

<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js">
</script>

<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js">
</script>

<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js">
</script>

</head>
<body>


<script type="text/javascript" language="javascript">

$(document).ready(function(){
  refreshTable();
});

function refreshTable(){
    $('#myModal').load('property-detailed.php #myModal', function() {
       setTimeout(refreshTable, 1000);
    });
}
</script>


<div id="myModal"></div>
 <!-- 


<div class="modal" id="print_mesg">
    <div class="modal__body"><span data-i18n="printing"></span></div>
</div>

<div class="modal" id="modal_mesg">
</div>



<div class="modalmia" id="modal_mia">
</div> -->

</body>
</html>









