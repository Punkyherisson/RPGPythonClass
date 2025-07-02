# Obtenir la date du jour au format YYYY-MM-DD
$today = Get-Date -Format "yyyy-MM-dd"

# Récupérer la branche Git actuelle
$currentBranch = git rev-parse --abbrev-ref HEAD

# Demander le nom de la branche (défaut : branche actuelle)
$branchName = Read-Host "Branche de push [$currentBranch]"
if ([string]::IsNullOrWhiteSpace($branchName)) {
    $branchName = $currentBranch
}

# Demander le message de commit
$message = Read-Host "Que fait cette version ?"

# Formater le message final avec la date
$fullMessage = "$today $message"

# Étapes Git
git add .
git commit -m "$fullMessage"
git tag "$fullMessage"
git push origin $branchName
git push origin --tags

Write-Host "`n✅ Commit envoyé sur [$branchName] avec le tag : $fullMessage"
Pause