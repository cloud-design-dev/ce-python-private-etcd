push-and-follow: gh-push gh-watch 

gh-watch: gh-run-watch ce-submit-job

gh-push:
	git add . && git commit -m "Building new container image" && git push

gh-run-list:
	gh run list --workflow="ICR Image build and push" --limit 1

gh-run-watch:
	sleep 10; gh run watch && echo "Container has been built and pushed to registry."

ce-submit-job:
	echo "Submitting job run to Code Engine"
	
	ibmcloud ce jobrun submit --name $$(date +%Y%m%d%H%M%S)-run  --job $${JOB_NAME} 

	echo "Following jobrun logs" 

	ibmcloud ce jobrun logs -f -n $$(ibmcloud ce jobrun list -s age --job $${JOB_NAME} --output json | jq -r '.items[0].metadata.name')

