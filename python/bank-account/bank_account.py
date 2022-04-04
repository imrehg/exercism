"""Welcome to Exercism Banking, Ltd."""

import threading


class BankAccount:
    """Bank account implementation with balance tracking
    and manipulation, as well as other required services.
    Threadsafe.
    """

    def __init__(self):
        """Create a bank account."""
        # The account starts out closed
        self.balance = 0
        self.is_open = False
        # Account-global lock to allow threadsafe processing
        self._lock = threading.Lock()

    def __check_account_state(self, required_open: bool = True):
        """Checks if the account's state is as requested.

        Args:
            required_open: toggle whether to check if the account is open (True/default),
                         or closed

        Raises:
            ValueError: if the account is not in the required state

        Returns:
            None
        """
        if self.is_open != required_open:
            raise ValueError("Account action is not permitted in its current state.")

    def open(self):
        """Opens or reopens the account and resets balance.

        Args:
            None

        Raises:
            ValueError: if the account is not closed

        Returns:
            None
        """
        with self._lock:
            # Account check
            self.__check_account_state(required_open=False)
            # Reset account state to the basics
            self.balance = 0
            self.is_open = True

    def get_balance(self) -> int:
        """Get the current balance of the account

        Args:
            None

        Raises:
            ValueError: if the account is not open

        Returns:
            The account balance value.
        """
        with self._lock:
            # Account check
            self.__check_account_state()
            return self.balance

    def deposit(self, amount: int):
        """Deposit an amount into the account

        Args:
            amount: the amount to deposit

        Raises:
            ValueError: if the account is not open
            ValueError: if a deposit of negative amount is attempted

        Returns:
            None
        """
        with self._lock:
            # Account check
            self.__check_account_state()
            # Input checks
            if amount < 0:
                raise ValueError(f"Cannot deposit negative amount: {amount}.")
            self.balance += amount

    def withdraw(self, amount: int):
        """Withdraw an amount from the account

        Args:
            amount: the amount to withdraw

        Raises:
            ValueError: if the account is not open
            ValueError: if a withdrawal of negative amount is attempted
            ValueError: if a withdrawal larger than the current balance is attempted

        Returns:
            None
        """
        with self._lock:
            # Account check
            self.__check_account_state()
            # Input checks
            if amount < 0:
                raise ValueError(f"Cannot withdraw negative amount: {amount}.")
            if self.balance < amount:
                raise ValueError("Cannot withdraw more than balance.")
            self.balance -= amount

    def close(self):
        """Close the given account

        Args:
            None

        Raises:
            ValueError: if the account is not open

        Returns:
            None
        """

        with self._lock:
            self.__check_account_state()
            # Close the account
            self.is_open = False
