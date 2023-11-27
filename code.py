@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        payload = request.get_json()
        event_type = request.headers.get('X-GitHub-Event')

        # Print debugging information
        print(f"Received GitHub event type: {event_type}")
        print(f"Received payload: {payload}")

        if event_type == 'pull_request':
            # Extract relevant information from the webhook payload
            repository_name = payload['repository']['full_name']
            pull_number = payload['pull_request']['number']

            # Call the function to process the pull request
            process_pull_request(repository_name, pull_number)

            return jsonify({'message': 'Webhook received successfully'}), 200
        else:
            return jsonify({'message': f'Ignoring unsupported event type: {event_type}'}), 200

    except Exception as e:
        print(f'Error processing webhook: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

