
import pytest
from rollup import process_rollup

def test_process_rollup(mocker):
    mock_contract = mocker.Mock()
    mock_contract.functions.submitRollup.return_value.transact.return_value = b'0x1234'

    mocker.patch('rollup.contract', mock_contract)
    mocker.patch('rollup.w3.eth.wait_for_transaction_receipt', return_value={'status': 1})

    transactions = [
        {"signer": "0x1111", "function": "func1", "cost": 0.1, "timestamp": 1234567890, "params": {}},
        {"signer": "0x2222", "function": "func2", "cost": 0.2, "timestamp": 1234567891, "params": {}},
        {"signer": "0x1111", "function": "func3", "cost": 0.3, "timestamp": 1234567892, "params": {}}
    ]

    receipt = process_rollup(transactions)

    assert receipt['status'] == 1
    mock_contract.functions.submitRollup.assert_called_once()
    args = mock_contract.functions.submitRollup.call_args[0]
    assert args[0] == ["0x1111", "0x2222"]
    assert args[1] == [0.4, 0.2]
